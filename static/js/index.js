const container=document.querySelector(".container")

const movie=document.querySelector('#movie')
// const count=document.querySelector(".count")
const total=document.querySelector(".total")
// console.log(seats);


//获取总价和数量
function updateSelectedCount(){
    const selected = document.querySelectorAll('.container .selected')
    // console.log(selected.length*+movie.value);
    // count.innerHTML=selected.length
    // total.innerHTML=(selected.length*+movie.value).toFixed(2)
}

//选电影座位
container.addEventListener('click',e=>{

    // console.dir();
    if(e.target.classList.contains('seat')&&
    !e.target.classList.contains('occupied')&&
    !e.target.classList.contains('disabled')){
        if(e.target.classList.contains('selected')) {
            const username = document.getElementById("username").value
            $.ajax({
                type: 'GET',
                url: '/deal_seat?type=0&seat='+e.target.id+'&username='+username,
                // 获得数据，从响应头中获取Location
                success: function(data, status, request) {
                    // status_url = request.getResponseHeader('Location');
                    // 调用 update_progress() 方法更新进度条
                    // update_progress(status_url, nanobar, div[0]);
                },
                error: function() {
                    alert('Unexpected error');
                }
            });
            e.target.classList.remove('selected')
        }else {
            const selected = document.querySelectorAll('.container .selected')
            if(selected.length >= 3){
                alert('选择座位不能超过3个');
                return
            }
            const username = document.getElementById("username").value
            $.ajax({
                type: 'GET',
                url: '/deal_seat?type=1&seat='+e.target.id+'&username='+username,
                // 获得数据，从响应头中获取Location
                success: function(data, status, request) {
                    // status_url = request.getResponseHeader('Location');
                    // 调用 update_progress() 方法更新进度条
                    // update_progress(status_url, nanobar, div[0]);
                    if(data == 'ok'){
                        e.target.classList.add('selected')
                    }else {
                        alert(data);
                        e.target.classList.add('occupied');
                    }

                },
                error: function() {
                    alert('Unexpected error');
                }
            });

        }

        console.log(e.target.id);


    }
    // updateSelectedCount()
})

//选电影的场次
// movie.addEventListener('change',e=>{
//     updateSelectedCount()
// })

updateSelectedCount()
