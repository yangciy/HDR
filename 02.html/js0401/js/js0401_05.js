//입력받은 점수가 90점이상이면 A 

let num = prompt('점수를 입력하세요.','100')

if(num>=90){
    document.write('A입니다.')
}else if(num>=80){
    document.write('B입니다.')
}else if(num>=70){
    document.write('C입니다.')
}else if(num>=60){
    document.write('D입니다.')
}else{
    document.write('F입니다.')
}