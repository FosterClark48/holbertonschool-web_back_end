// Task 4 - Test cases

const sinon = require('sinon');
const expect = require('chai').expect;
const sendPaymentRequestToApi = require('./4-payment');
const Utils = require('./utils');

describe('sendPaymentRequestToApi with stub', () => {
  it('should call Utils.calculateNumber with correct arguments and log the correct message', () => {
    // Stubbing Utils.calculateNumber to always return 10
    const stub = sinon.stub(Utils, 'calculateNumber').returns(10);

    // Spying on console.log
    const logSpy = sinon.spy(console, 'log');

    sendPaymentRequestToApi(100, 20);

    // Verifying that the stub is called with the expected arguments
    expect(stub.calledOnce).to.be.true;
    expect(stub.calledWith('SUM', 100, 20)).to.be.true;

    // Verifying that console.log is logging the correct message
    expect(logSpy.calledWith('The total is: 10')).to.be.true;

    // Restoring the stub and spy
    stub.restore();
    logSpy.restore();
  });
});
