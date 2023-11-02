// Task 3 - Spies utils

const Utils = {
  calculateNumber(type, a, b) {
    const roundedA = Math.round(a);
    const roundedB = Math.round(b);

    switch (type) {
      case 'SUM':
        return roundedA + roundedB;
      case 'SUBTRACT':
        return roundedA - roundedB;
      case 'DIVIDE':
        if (roundedB === 0) return 'Error';
        return roundedA / roundedB;
      default:
        return 'Error';
    }
  }
};

module.exports = Utils;
