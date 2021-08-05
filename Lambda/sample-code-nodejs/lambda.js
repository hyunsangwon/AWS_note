const AWS = require("aws-sdk");
const moment = require("moment");
const docClient = new AWS.DynamoDB.DocumentClient();

///IoTCore에서 받아온 데이터를 DynamoDB에 저장하는 프로세스 코드
exports.handler = async (event) => {
    console.log("device id ==> " + event["device_id"]);
    console.log("reported_temperature ==> " + event["reported_temperature"]);
    let params = {
        TableName: process.env.TABLE_NAME,
        Item: {
            device_id: String(event["device_id"]),
            received_at: moment().add(9, "h").format("YYYY-MM-DD HH:mm:ss.SSS"),
            temperature: event["reported_temperature"],
            comment: event["comment"],
        },
    };
    try {
        await createItem(params);
        return { body: "Successfully created item!" };
    } catch (err) {
        return { error: err.message };
    }
};

const createItem = async (params) => {
    try {
        await docClient.put(params).promise();
    } catch (err) {
        console.log("createItem ===> " + err);
        return err;
    }
};
