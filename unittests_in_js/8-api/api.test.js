// Task 8 - Express app test suite

const chai = require('chai');
const chaiHttp = require('chai-http');
const expect = chai.expect;
chai.use(chaiHttp);

const serverAddress = 'http://localhost:7865';

describe('Index page', () => {
  it('should return status 200', (done) => {
    chai.request(serverAddress)
      .get('/')
      .end((err, res) => {
        expect(res).to.have.status(200);
        done();
      });
  });

  it('should return the correct content', (done) => {
    chai.request(serverAddress)
      .get('/')
      .end((err, res) => {
        expect(res.text).to.equal('Welcome to the payment system');
        done();
      });
  });
});
