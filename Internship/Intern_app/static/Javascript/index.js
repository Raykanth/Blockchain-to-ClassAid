import { ethers } from "./ethers-5.6.esm.min.js";
import { abi, contractAddress } from "./constants.js";
// import { Student_id } from "views";

const connectButton = document.getElementById("connectButton");
connectButton.onclick = connect;
async function connect() {
  if (typeof window.ethereum !== "undefined") {
    try {
      await ethereum.request({ method: "eth_requestAccounts" });
    } catch (error) {
      console.log(error);
    }
    connectButton.innerHTML = "Connected";
    // console.log("plplp", Student_id);
    console.log("CONN");
    fund.call();
    console.log("NECTED");
    // const ethAmount = "0.75";
    // const provider = new ethers.providers.Web3Provider(window.ethereum);
    // const signer = provider.getSigner();
    // const contract = new ethers.Contract(contractAddress, abi, signer);
    // try {
    //   const transactionResponse = await contract.fund({
    //     value: ethers.utils.parseEther(ethAmount),
    //   });
    //   await listenForTransactionMine(transactionResponse, provider);
    // } catch (error) {
    //   console.log(error);
    // }
    // const accounts = await ethereum.request({ method: "eth_accounts" });
    // console.log(accounts);
  } else {
    connectButton.innerHTML = "Please install MetaMask";
  }
}

async function fund() {
  const ethAmount = "0.85";
  if (typeof window.ethereum !== "undefined") {
    const provider = new ethers.providers.Web3Provider(window.ethereum);
    const signer = provider.getSigner();
    const contract = new ethers.Contract(contractAddress, abi, signer);
    try {
      const transactionResponse = await contract.fund({
        value: ethers.utils.parseEther(ethAmount),
      });
      console.log("CONNECTED");
      await listenForTransactionMine(transactionResponse, provider);
    } catch (error) {
      console.log(error);
    }
  } else {
    fundButton.innerHTML = "Please install MetaMask";
  }
}
