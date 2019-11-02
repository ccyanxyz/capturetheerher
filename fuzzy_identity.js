const util = require('ethereumjs-util');
const rlp = require('rlp');
const generate = require('ethjs-account').generate;
seed='892h@fs8sk^2hSFR*/8s8shfs.jk39hsoi@hohskd51D1Q8E1%^;DZ1-=.@WWRXNI()VF6/*Z%$C51D1QV*<>FE8RG!FI;"./+-*!DQ39hsoi@hoFE1F5^7E%&*QS'
function fuzz(){
    for(var k=0;k<50000;k++){
        seed=seed+Math.random().toString(36).substring(12);
        for(var i=0;i<1000;i++){
            res=generate(seed);
            for (var j=0;j<10;j++){
                encodedRlp = rlp.encode([res.address, j]);
                buf = util.keccak256(encodedRlp);
                contractAddress =buf.slice(12).toString('hex');
                if(contractAddress.match("badc0de")){
                    console.log(res);
                    console.log(j);
                    return;
                }
            }
        }
    }
}
fuzz();
