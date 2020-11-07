const pengsu = {
    name: '펭수',
    'phone number' : '01012345678',
    profile : {
        dream: '우주대스타',
        age: '11살',
        seciality: '요들송',
    }
}

// Object => JSON 변환

let objJson = JSON.stringify(pengsu)

console.log(objJson) // {"name":"펭수","phone number":"01012345678","profile":{"dream":"우주대스타","age":"11살","seciality":"요들송"}}
console.log(typeof objJson) // string

// JSON => Object 변환

let jsonObj = JSON.parse(objJson)

console.log(jsonObj)
/*{
  name: '펭수',
  'phone number': '01012345678',
  profile: { dream: '우주대스타', age: '11살', seciality: '요들송' }
}*/
console.log(typeof jsonObj) // object
