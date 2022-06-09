import fetch from "node-fetch"

const getData = async (next) => {
    const response = await fetch(next)
    const data = await response.json()
    return data
}

var next = 'https://swapi.dev/api/people'

console.log("People...")

while (next && next.length > 0) {
    var data = await getData(next)
    console.log(data.results.length +" - "+ data.next)
    next = data.next
}

console.log("People...Finished")
