export default class Building {
  constructor(sqft) {
    if (this.constructor !== Building && !this.evacuationWarningMessage) {
      throw new Error('Class extending Building must override evacuationWarningMessage');
    }
    this.sqft = sqft;
  }

  get sqft() {
    return (this._sqft);
  }

  set sqft(value) {
    if (typeof value !== 'number') {
      throw new TypeError('sqft must be a Number');
    }
    this._sqft = value;
  }
}
