var n =1
function gallery(num){
    //5이상이 되면 1로 갈 수 있도록 프로그램하라
    //1 이하로가면 5로 변경시켜라
    
    n += num
    // let a = document.getElementById("photo").getAttribute("src")
    if(n>5)
        n=1
    else if(n<1)
        n=5
    let a = document.getElementById("photo")
    a.setAttribute("src","images/"+(n)+'.jpeg')
    //attr
    document.getElementById('viewNum').innerText=n;
    
}







// let adminId = 'admin';
// let adminPw = '1111';


// function loginBtn(){
//     let uid = prompt('아이디를 입력하세요.');
//     let upw = prompt('패스워드를 입력하세요.');
  
//     login(uid,upw);  //login 함수 호출(매개변수 전달)

// }

// function login(uid,upw){
//     if(uid == adminId && upw == adminPw){
//         alert('로그인 성공')
//         location.href='https://www.naver.com';
//     }else{
//         alert('아이디 또는 비밀번호가 일치하지 않습니다.')
//     }
// }








// function sum1(){
//     let sum=0;
//     let a = parseInt(prompt('숫자를 입력하세요.','0'));
//     let b = parseInt(prompt('숫자를 입력하세요.','0'));
//     //1~10까지의 합을 출력하는 함수
//     if (a>b){
//         for(let i=b;i<=a;i++){
//             sum +=i;
//         }
//     }
//     document.write(a+"부터"+b+"까지 합: "+sum);
// }