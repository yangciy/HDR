let id = prompt('아이디를 입력하세요.');
let pw = prompt('패스워드를 입력하세요.')
let count=0


if (count<3){

    if (id=='admin')
        if(pw=='1111'){
            document.write('아이디와 패스워드 일치')
            location.href='http://www.naver.com'}
        else{
            document.write('패스워드가 틀렸습니다.')
            count++
            alert('패스워드가 일치하지 않습니다. 다시입력하세요.')
            location.reload()
            }
    else{
        document.write('아이디가 일치하지 않습니다.')
        
        alert('아이디가 일치하지 않습니다. 다시입력하세요.')
        count++
        location.reload()
        }
    }
document.write('2번이상 틀렸다는거야 종료한다.')

