
function fetch_api(){
    let id = document.getElementById("js").value;
    console.log(id);

    fetch('https://reqres.in/api/users/'+id).then(
        response => response.json()
    ).then(
        response_obj => put_users_inside_html(response_obj.data)
    ).catch(
        err => console.log(err)
    )
}

function put_users_inside_html(response_obj_data) {

    const current_main = document.querySelector("div");
    current_main.innerHTML = `
    <img src="${response_obj_data.avatar}" alt="avatar"/>
    <div>
        <span>id : ${response_obj_data.id}</span><br>
        <span>email: ${response_obj_data.email}</span><br>
        <span>full name : ${response_obj_data.first_name} ${response_obj_data.last_name}</span><br>

    </div>
    `;

}
