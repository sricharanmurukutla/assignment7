// Lambda function handler
export const handler = async (event) => {
    // Safely extract the keyword from query string parameters
    const keyword = event.queryStringParameters ? event.queryStringParameters.keyword : null;

    // Check if the keyword exists
    if (!keyword) {
        return {
            statusCode: 400,
            body: JSON.stringify({ message: "No keyword provided" }),
        };
    }

    // Construct and return the response
    const response = {
        statusCode: 200,
        body: JSON.stringify(`Sri Charan Murukutla says: ${keyword}`),
    };

    return response;
};

