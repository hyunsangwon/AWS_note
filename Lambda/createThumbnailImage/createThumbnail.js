const async = require('async');
const AWS = require('aws-sdk');
let gm = require('gm')
    .subClass({ imageMagick: true }); // Enable ImageMagick integration.
const util = require('util');

// 섬네일 사이즈 기본값
const MAX_WIDTH  = 200;
const MAX_HEIGHT = 200;

let s3 = new AWS.S3();

exports.handler = (event, context, callback) => {
    // Read options from the event.
    let srcBucket = event.Records[0].s3.bucket.name;
    // Object key may have spaces or unicode non-ASCII characters.
    let srcKey    =
        decodeURIComponent(event.Records[0].s3.object.key.replace(/\+/g, " "));
    let dstBucket = srcBucket; // ***실제 저장될 버킷
    let dstKey    = "thumbs/" + srcKey; // ***실제 저장될 데이터

    // Infer the image type.
    let typeMatch = srcKey.match(/\.([^.]*)$/);

    if (!typeMatch) {
        callback("Could not determine the image type.");
        return;
    }
    let imageType = typeMatch[1].toLowerCase();
    if (imageType != "jpg" && imageType != "png") {
        callback(`Unsupported image type: ${imageType}`);
        return;
    }

    //waterfall 함수를 이용하여 차례로 여러번 함수 실행
    async.waterfall([
            function download(next) {
                // Download the image from S3 into a buffer.
                s3.getObject({
                        Bucket: srcBucket,
                        Key: srcKey
                    },
                    next);
            },
            function transform(response, next) {
                gm(response.Body).size(function(err, size) {
                    // Infer the scaling factor to avoid stretching the image unnaturally.
                    let scalingFactor = Math.min(
                        MAX_WIDTH / size.width,
                        MAX_HEIGHT / size.height
                    );
                    let width  = scalingFactor * size.width;
                    let height = scalingFactor * size.height;

                    // Transform the image buffer in memory.
                    this.resize(width, height)
                        .toBuffer(imageType, function(err, buffer) {
                            if (err) {
                                next(err);
                            } else {
                                next(null, response.ContentType, buffer);
                            }
                        });
                });
            },
            function upload(contentType, data, next) {
                // Stream the transformed image to a different S3 bucket.
                s3.putObject({
                        Bucket: dstBucket,
                        Key: dstKey,
                        Body: data,
                        ContentType: contentType
                    },
                    next);
            }
        ], (err)=> {
            if (err) {
                console.error(
                    'Unable to resize ' + srcBucket + '/' + srcKey +
                    ' and upload to ' + dstBucket + '/' + dstKey +
                    ' due to an error: ' + err
                );
            } else {
                console.log(
                    'Successfully resized ' + srcBucket + '/' + srcKey +
                    ' and uploaded to ' + dstBucket + '/' + dstKey
                );
            }

            callback(null, "message");
        }
    );
};
