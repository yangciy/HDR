let site =prompt('원하는 번호를 클릭하세요.\n 1.naver 2.daum 3.goole' )
document.write(site);


switch(site){
    case '1' :
        alert('네이버를 선택했습니다.');
        location.href='https://www.naver.com'
    break;

    case '2' :
        alert('다음을 선택했습니다.');
        location.href='https://www.daum.net'
    break;

    case '3' :
        alert('구글을 선택했습니다.');
        location.href='https://www.google.co.kr'
    break;

    default:
        alert('잘못선택했습니다.');
    break

}