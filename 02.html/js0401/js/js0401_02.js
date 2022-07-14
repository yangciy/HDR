let a =10;
let b = 3;
let c = 5;

// 삼항식
var result = (a>b)?'a가 더 큽니다.':'b가 더 큽니다.';
let result2 = (a>b)?a:b;
let result1 =''
if(a>b){
    result1='a가 더 큽니다.!';
}else{
    result1='b가 더 큽니다.';
}
document.write(result1+'<br>');
document.write(result2+'<br>');
document.write(result+'<br>');
document.write(a+','+b+' 중에 더 큰수는 ?'+result2+'<br>')
let sum = 0;
for(let i=1;i<10;i++){
    sum +=i;
}
document.write('sum의 값 : '+sum);