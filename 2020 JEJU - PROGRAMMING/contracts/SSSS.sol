pragma solidity >=0.4.22 <0.8.0;


contract SSSS {
    string public greeting;
    int private _X;
    int private _Y;
    
    constructor() public {
        greeting = 'Hello';
    }
    
    function clearMap() public {
        _X = 0;
        _Y = 0;
    }

    function setMap(int _x, int _y) public {
        _Y =  _y;
        _X = _x;
    }
/*
    function getMap(uint _x) view public returns (uint) {
        return da[_x];
    }
*/
}
