
const apiKey = "8374f8c80936aec0e5aa";
let requestvalue = "";
function request(d_un,d_deux){
    const url = 'https://free.currconv.com/api/v7/convert?q=' + d_un + '_' + d_deux + '&compact=ultra&apiKey=' + apiKey;
    return fetch(url)
    .then((response) => {
        return response.json();
    })
    .then((response) => {
        return response;
    })
    .catch(err => {
        console.log(err);
    });
}

async function let(d_un, d_deux, variable){
    return await request(d_un, d_deux).then(
        (res) => {
            variable = res;
            let devises = d_un + '_' + d_deux;
            variable = variable[devises];
            return variable;
        }
    )
}

async function fcadeur(){
    let tempvar = await let('CAD','EUR', 'cadeur');
    return tempvar
}
async function fcadusd(){
    let tempvar = await let('CAD','USD', 'cadusd');
    return tempvar
}
async function fchfeur(){
    let tempvar = await let('CHF','EUR', 'chfeur');
    return tempvar
}
async function fchfgbp(){
    let tempvar = await let('CHF','GBP', 'chfgbp');
    return tempvar
}
async function faudsgd(){
    let tempvar = await let('AUD','SGD', 'audsgd');
    return tempvar
}
async function fgipeur(){
    let tempvar = await let('GIP','EUR', 'gipeur');
    return tempvar
}
async function feurxpf(){
    let tempvar = await let('EUR','XPF', 'eurxpf');
    tempvar = tempvar*50;
    return tempvar
}
async function fdkkisk(){
    let tempvar = await let('DKK','ISK', 'dkkisk');
    return tempvar
}
async function fnoksek(){
    let tempvar = await let('NOK','SEK', 'noksek');
    tempvar = tempvar*1000;
    return tempvar
}
async function fkrweur(){
    let tempvar = await let('KRW','EUR', 'krweur');
    return tempvar
}



async function mainMoney(){
    //api calls
    let cadeur = await fcadeur();
    let cadusd = await fcadusd();
    let chfeur = await fchfeur();
    let chfgbp = await fchfgbp();
    let audsgd = await faudsgd();
    let gipeur = await fgipeur();
    let eurxpf = await feurxpf();
    let dkkisk = await fdkkisk();
    let noksek = await fnoksek();
    let krweur = await fkrweur();
    //results

    let pndchf = cadusd + cadeur;
    let pnd = pndchf*chfeur;
    
    let fcdgip = pndchf - chfgbp - cadeur + audsgd;
    let fcd = fcdgip*gipeur;

    let evckrw = eurxpf - dkkisk + noksek;
    let milevc = evckrw*krweur;
    let evc = (milevc)/1000;

    let pndtext = document.querySelector('.pnd strong');
    let fcdtext = document.querySelector('.fcd strong');
    let evctext = document.querySelector('.evc strong');

    pndtext.textContent = pnd;

    fcdtext.textContent = fcd;

    evctext.textContent = milevc;

    let start = "EUR";
    let end = "EUR"

    const starta = document.getElementsByClassName("Start")[0];
    starta.addEventListener("change", function(){
        let choice = starta.selectedIndex;
        start = starta.options[choice].text;
    });


    const enda = document.getElementsByClassName("End")[0];
    enda.addEventListener("change", function(){
        let choice = enda.selectedIndex;
        end = enda.options[choice].text;
    });

    const somme = document.getElementsByClassName("somme")[0];
    let result = 0;
    const output = document.querySelector('.output strong');
    
    let sommehtml = document.getElementsByClassName('somme');
    let sommei = sommehtml.textContent;
    console.log(sommei);

    function conv(rc){
        rc = parseInt(rc);
        if (start === 'EUR'){
            if (end === 'EUR'){
                result = rc;
                output.textContent = result;
            }else if (end === 'PND'){
                result = (1/pnd)*rc;
                output.textContent = result;
            }else if (end === 'FCD'){
                result = (1/fcd)*rc;
                output.textContent = result;
            }else if (end === 'EVC'){
                result = (1/evc)*rc;
                output.textContent = result;
            }
        }
        else if (start === 'PND'){
            if (end === 'PND'){
                result = rc;
                output.textContent = result;
            }else if (end === 'EUR'){
                result = pnd*rc;
                output.textContent = result;
            }else if (end === 'FCD'){
                result = pnd/fcd*rc;
                output.textContent = result;
            }else if (end === 'EVC'){
                result = pnd/evc*rc;
                output.textContent = result;
            }
        }
        else if (start === 'FCD'){
            if (end === 'FCD'){
                result = rc;
                output.textContent = result;
            }else if (end === 'EUR'){
                result = fcd*rc;
                output.textContent = result;
            }else if (end === 'PND'){
                result = fcd/pnd*rc;
                output.textContent = result;
            }else if (end === 'EVC'){
                result = fcd/evc*rc;
                output.textContent = result;
            }
        }
        else if (start === 'EVC'){
            if (end === 'EVC'){
                result = rc;
                output.textContent = result;
            }else if (end === 'EUR'){
                result = evc*rc;
                output.textContent = result;
            }else if (end === 'PND'){
                result = evc/pnd*rc;
                output.textContent = result;
            }else if (end === 'FCD'){
                result = evc/fcd*rc;
                output.textContent = result;
            }
        }
    }
    
    somme.addEventListener('input', function(event) {
        let rc = event.target.value;
        conv(rc)
    });
    
    const valider = document.getElementById("valider");

    valider.addEventListener('click', () => {
        conv(sommei);
    });

}
mainMoney()
