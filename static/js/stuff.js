const drop = () => {
    const things = document.getElementById("drop")
    things.style.display = "block"
}

const cutie = () => {
    let cutieButton = document.getElementById("cutiebutton")
    cutieButton.innerHTML = "Welp. You didn't listen. Now you're a huge cutie. Check your console for more info."
    cutieButton.disabled = true
    cutieButton.style.textDecoration = "none"
    console.warn("So it appears you've clicked the button you've been told not to click. You don't like to listen so you've been deemed a cutie, although i think you're quite adorable to be honest. If you didn't want this should've listened you big cutie.")
    /* let s = document.createElement('style')
    let css = `button:hover {
        transition: none;
        transform: none;
        text-decoration: none;
        color: rgb(204, 204, 204);
    }`
    if (s.styleSheet) {
        s.styleSheet.cssText = css;
    } else {
        s.appendChild(document.createTextNode(css))
    }
    document.getElementsByTagName('head')[0].appendChild(style) */
    
}

const dots = () => {window.setInterval(() => {
        let wait = document.getElementById("wait")
        if (wait.innerHTML.length > 2) wait.innerHTML = ""
        else wait.innerHTML += "."
    }, 200)
}