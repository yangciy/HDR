let num = parseInt(prompt('숫자를 입력하세요.','0'));

if(num%2==0){
    document.write('짝수입니다.'+'<br>')
}else{
    document.write('홀수입니다.'+'<br>')
}

result = parseInt(num/7)
result2  = num%7

document.write(num+'/7의 몫 : '+ result+'나머지 :'+result2)



// let num =10;
// if(num>10)
// document.write('10보다 큽니다.')
// else
// document.write('10보다 작거나 같습니다.')