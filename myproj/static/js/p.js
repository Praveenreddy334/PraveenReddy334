const loading= () =>{
    const filedrop=document.querySelector(".filedrop");
    function active(){
    filedrop.classList.add("border-success")
    }
    const prevents = (e) => e.preventDefault();

    ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(evtName => {
        filedrop.addEventListener(evtName, prevents);
    });
    function inactive(){
        filedrop.classList.remove("border-success")
    }
     ['dragenter', 'dragover'].forEach(evtName => {
            filedrop.addEventListener(evtName, active);
         });
    ['dragleave','drop'].forEach(evtName=>{
        filedrop.addEventListener(evtName, inactive);
    })
    filedrop.addEventListener("drop",fileContent);
}
const fileContent=(e)=>{
    const d=e.dataTransfer;
    const files= d.files;
    console.log(files);
}
document.addEventListener("DOMContentLoaded", loading);

