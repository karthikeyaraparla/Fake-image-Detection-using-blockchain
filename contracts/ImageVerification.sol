// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

contract ImageVerification {
    struct Image {
        string hash;
        bool isFake;
        address uploader;
        uint256 timestamp;
    }

    mapping(string => Image) public images;
    
    event ImageStored(string hash, bool isFake, address uploader, uint256 timestamp);

    function storeImage(string memory _hash, bool _isFake) public {
        images[_hash] = Image({
            hash: _hash,
            isFake: _isFake,
            uploader: msg.sender,
            timestamp: block.timestamp
        });
        
        emit ImageStored(_hash, _isFake, msg.sender, block.timestamp);
    }

    function verifyImage(string memory _hash) public view returns (bool isFake, address uploader, uint256 timestamp) {
        Image memory img = images[_hash];
        return (img.isFake, img.uploader, img.timestamp);
    }
}
