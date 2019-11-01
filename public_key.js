const EthereumTx = require('ethereumjs-tx');

const rawTx = "0xf87080843b9aca0083015f90946b477781b0e68031109f21887e6b5afeaaeb002b808c5468616e6b732c206d616e2129a0a5522718c0f95dde27f0827f55de836342ceda594d20458523dd71a539d52ad7a05710e64311d481764b5ae8ca691b05d14054782c7d489f3511a7abf2f5078962";

let tx = new EthereumTx(rawTx);

console.log('0x' + tx.getSenderPublicKey().toString('hex'));
