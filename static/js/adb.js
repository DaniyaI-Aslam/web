
async function detectAdBlock() {
    let adBlockEnabled = false
    const googleAdUrl = 'https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js'
    try {
        await fetch(new Request(googleAdUrl)).catch(_ => adBlockEnabled = true)
        

    } catch (e) {
        adBlockEnabled = true
    } finally {
        console.log(`AdBlock Enabled: ${adBlockEnabled}`)
        if (adBlockEnabled === true) {
            document.getElementById("twoo").style.pointerEvents = "none";
            wrapper.classList.add("show");
            // const gradient_background = document.querySelector('.gradient-background');

            // change text color to white
            // gradient_background.style.color = 'white';
        }
    }
}
detectAdBlock();
const detect = document.querySelector("#detect");
const wrapper = document.querySelector(".wrapper");
const button = wrapper.querySelector("button");
let adClasses = ["ad", "ads", "adsbox", "doubleclick", "ad-placement", "ad-placeholder", "adbadge", "BannerAd"];
for (let item of adClasses) {
    detect.classList.add(item);
}
let getProperty = window.getComputedStyle(detect).getPropertyValue("display");
if (!wrapper.classList.contains("show")) {
    // document.getElementById("twoo").style.pointerEvents = "none";
    getProperty == "none" ? wrapper.classList.add("show") : wrapper.classList.remove("show");
    // const gradient_background = document.querySelector('.gradient-background');

            // change text color to white
    //         gradient_background.style.color = 'white';
    //         document.getElementById(".gradient-background").style.zIndex = "100";

    // const bb = document.querySelector('body');
    // bb.style.pointerEvents = "none";
    
}


