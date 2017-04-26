function getConfirmation(){
    if (window.confirm("Are you sure you want to edit this post?")) { 
        document.location.replace('edit');  
    }
}

function postSaved(){
    alert('Post Saved!');
}
