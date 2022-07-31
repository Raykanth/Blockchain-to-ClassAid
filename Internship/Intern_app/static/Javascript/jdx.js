import { ethers } from "./ethers-5.6.esm.min.js";

const connectButton = document.getElementById("bbb");
bbb.onclick = connect;
async function connect() {
  if (typeof window.ethereum !== "undefined") {
    try {
      await ethereum.request({ method: "eth_requestAccounts" });
      const provider = new ethers.providers.Web3Provider(window.ethereum);
      const signer = provider.getSigner();
      const address = "0xf8e81D47203A594245E36C48e151709F0C19fBe8";
      const abi = [
        {
          inputs: [],
          name: "abc",
          outputs: [],
          stateMutability: "nonpayable",
          type: "function",
        },
      ];
      const contract = new ethers.Contract(address, abi, signer);
      try {
        const transactionResponse = await contract.abc({
          value: ethers.utils.parseEther("0"),
        });
        console.log("CONNECTED");
        await listenForTransactionMine(transactionResponse, provider);
      } catch (error) {
        console.log(error);
      }
    } catch (error) {
      console.log(error);
    }
  } else {
    connectButton.innerHTML = "Please install MetaMask";
  }
}
