const hre = require("hardhat");

async function main() {
    console.log("Deploying ImageVerification contract...");

    const imageVerification = await hre.ethers.deployContract("ImageVerification");
    await imageVerification.waitForDeployment();

    console.log(`ImageVerification contract deployed to: ${imageVerification.target}`);

    const [isFake, uploader, timestamp] = await imageVerification.verifyImage("imagehash123");
    console.log("Is Fake?", isFake);
    console.log("Uploader:", uploader);
    console.log("Timestamp:", new Date(Number(timestamp) * 1000).toLocaleString());
}

main().catch((error) => {
    console.error(error);
    process.exitCode = 1;
});
