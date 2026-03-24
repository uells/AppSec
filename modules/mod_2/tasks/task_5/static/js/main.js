// Общие функции
// Отправка post запроса
async function post(url, options) {
    try {
        let response =  await fetch(url, {
            'method': 'POST',
            'headers': {
                'Content-type': 'application/json'
            },
            'body': JSON.stringify(options)
        })
        if (!response.ok) {
            throw new Error("HTTP error")
        }
        let contentType = response.headers.get('content-type')
        if (!contentType || contentType.includes('application/json')) {
            throw new TypeError("Response is't JSON")
        }
        return await response.json()
    } catch (error) {
        console.log(`${endpoint}: ${error}`)
    }
}

// Чат
// Функция для отправки сообщения

