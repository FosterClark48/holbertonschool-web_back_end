// Test cases for Task 2 - changing to use chai's expect instead of Node's assert

const expect = require('chai').expect;
const calculateNumber = require('./2-calcul_chai');

describe('calculateNumber', () => {
  describe('Type SUM', () => {
    it('should return the sum of rounded numbers', () => {
      expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
      expect(calculateNumber('SUM', 1.5, 3.7)).to.equal(6);
    });
  });

  describe('Type SUBTRACT', () => {
    it('should return the difference of rounded numbers', () => {
      expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4);
      expect(calculateNumber('SUBTRACT', 3.7, 1.5)).to.equal(2);
    });
  });

  describe('Type DIVIDE', () => {
    it('should return the division of rounded numbers', () => {
      expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2);
      expect(calculateNumber('DIVIDE', 4.5, 1.4)).to.equal(5);
    });

    it('should return Error when dividing by 0', () => {
      expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error');
    });
  });

  describe('Invalid type', () => {
    it('should return Error for invalid type', () => {
      expect(calculateNumber('INVALID', 1.4, 4.5)).to.equal('Error');
    });
  });
});
