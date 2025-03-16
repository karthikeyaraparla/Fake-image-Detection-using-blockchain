const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("Lock", function () {
    async function deployOneYearLockFixture() {
        const ONE_YEAR_IN_SECS = 365 * 24 * 60 * 60;
        const ONE_GWEI = 1_000_000_000;

        const lockedAmount = ONE_GWEI;
        const unlockTime = (await ethers.provider.getBlock("latest")).timestamp + ONE_YEAR_IN_SECS;

        const lock = await ethers.deployContract("Lock", [unlockTime], {
            value: lockedAmount,
        });

        return { lock, unlockTime, lockedAmount };
    }

    describe("Deployment", function () {
        it("Should set the right unlockTime", async function () {
            const { lock, unlockTime } = await deployOneYearLockFixture();

            expect(await lock.unlockTime()).to.equal(unlockTime);
        });

        it("Should set the right owner", async function () {
            const { lock } = await deployOneYearLockFixture();
            const [owner] = await ethers.getSigners();

            expect(await lock.owner()).to.equal(owner.address);
        });
    });
}); 