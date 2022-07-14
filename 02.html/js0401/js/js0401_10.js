//데이터 5개 입력
//제일 큰수 3개를 출력하시오.
let arr=[0,0,0,0,0]
for(let i=0; i<arr.length;i++)
arr[i]=parseInt(prompt('숫자를 입력하세요.','0'))

arr.sort(function(a,b){
    return b-a;
})

for(let i=0;i<3;i++){
    document.write(arr[i]+'<br>')
}


// let arr=[5,1,50,8,6,20,3];
// let arr1=[3,5,1,6,9]
// arr1.sort()
// arr.sort(function(a,b){
//     return b-a
// })

// document.write(arr+'<br>')
// document.write(arr1)





// let arr = [0,1,2,3,4,5,6,7,8,9]
// for (let i=0;i<arr.length;i++){
//     document.write(arr[i]+'<br>')
// }
// document.write('<br>')
// for(i in arr){
//     document.write(arr[i]+'<br>')
// }