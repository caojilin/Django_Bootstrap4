// Daniel Shiffman
// Neuro-Evolution Flappy Bird with TensorFlow.js
// http://thecodingtrain.com
// https://youtu.be/cdUNkwXx-I4

class Pipe {
  constructor() {
    this.spacing = 100;
    this.top = random(height / 6, (3 / 4) * height);
    this.bottom = height - (this.top + this.spacing);
    this.x = width;
    this.w = 80;
    this.speed = 6;
  }

  hits(bird) {
    if (bird.y-bird.radius < this.top || bird.y + bird.radius > height - this.bottom) {
      if ((bird.x+bird.radius) > this.x && (bird.x-bird.radius) < (this.x + this.w)){
        return true;
      }
    }
    return false;
  }

  show() {
    push();
    fill('green');
    rectMode(CORNER);
    rect(this.x, 0, this.w, this.top);
    rect(this.x, height - this.bottom, this.w, this.bottom);
    pop();
  }

  update() {
    this.x -= this.speed;
  }

  offscreen() {
    if (this.x < -this.w) {
      return true;
    } else {
      return false;
    }
  }
}
