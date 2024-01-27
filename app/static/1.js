
let fombut = document.getElementById('formbut')

fombut.onclick = f1
let vision = false

function f1() {
    let formvid = document.getElementById('formvid')
    if (!vision) {
        formvid.hidden = false
        vision = true
    } else {
        formvid.hidden = true
        vision = false
    }
}

