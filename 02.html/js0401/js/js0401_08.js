let sum=0;
let input=parseInt(prompt('숫자를 입력하세용...!!!'));
let i =1;

while(i<=input){

    if(i%2==1)
    document.write('<p class="a1">'+i+'</p>')
    else
    document.write('<p class="a2">'+i+'*</p>')
    i++
    

    
}
// 홀수 와 짝수 1부터 10까지  어떻게 할꺼냐면 홀수는 글자색을 빨강으로, 짝수는 파랑



// while(i<=input){
//     i++
//     if(i%5==0 || i%2==0)
//     continue;
  
//     sum +=i;
    
// }
// document.write(sum);