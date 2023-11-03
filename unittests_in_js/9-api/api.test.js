// Task 9 - Express app test suite

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

describe('Cart page', () => {
  it('should return status 200 for numeric id', (done) => {
    chai.request(serverAddress)
      .get('/cart/123')
      .end((err, res) => {
        expect(res).to.have.status(200);
        expect(res.text).to.equal('Payment methods for cart 123');
        done();
      });
  });

  it('should return status 404 for non-numeric id', (done) => {
    chai.request(serverAddress)
      .get('/cart/abc') // This should fail the numeric check
      .end((err, res) => {
        expect(res).to.have.status(404);
        done();
      });
  });
});
