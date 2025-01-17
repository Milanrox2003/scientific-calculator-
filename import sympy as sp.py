<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Calculator</title>
    <link rel="stylesheet" href="style.css" />
  </head>
  <body>
    <div id="calculator">
      <input type="text" id="output" value="0" />
      <div class="row">
        <button onclick="calc('(')" class="scientific laptop">(</button>
        <button onclick="calc(')')" class="scientific laptop">)</button>
        <button onclick="calc('mc')" class="scientific laptop">mc</button>
        <button onclick="calc('m+')" class="scientific laptop">m+</button>
        <button onclick="calc('m-')" class="scientific laptop">m-</button>
        <button onclick="calc('mr')" class="scientific laptop">mr</button>
        <button onclick="calc('C')" class="scientific">AC</button>
        <button onclick="calc()" class="scientific">+/-</button>
        <button onclick="calc('%')" class="scientific">%</button>
        <button onclick="calc('÷')" class="right">÷</button>
      </div>
      <div class="row">
        <button onclick="inverse()" id="secondary" class="scientific laptop">2<sup>nd</sup></button>
        <button onclick="calc('^2')" class="scientific laptop">x<sup>2</sup></button>
        <button onclick="calc('^3')" class="scientific laptop">x<sup>3</sup></button>
        <button onclick="calc('^')" class="scientific laptop">x<sup>y</sup></button>
        <button onclick="calc('e^')" class="scientific laptop">e<sup>x</sup></button>
        <button onclick="calc('10^')" class="scientific laptop">10<sup>x</sup></button>
        <button onclick="calc('7')">7</button>
        <button onclick="calc('8')">8</button>
        <button onclick="calc('9')">9</button>
        <button onclick="calc('×')" class="right">×</button>
      </div>
      <div class="row">
        <button onclick="calc('^-1')" class="scientific laptop">1/x</button>
        <button onclick="calc('^(1/2)')" class="scientific laptop">√x</button>
        <button onclick="calc('^(1/3)')" class="scientific laptop"><sup>3</sup>√x</button>
        <button onclick="calc('^(1/')" class="scientific laptop"><sup>y</sup>√x</button>
        <button onclick="calc('ln(')" class="scientific laptop">ln</button>
        <button onclick="calc('log(')" class="scientific laptop">log<sub>10</sub></button>
        <button onclick="calc('4')">4</button>
        <button onclick="calc('5')">5</button>
        <button onclick="calc('6')">6</button>
        <button onclick="calc('-')" class="right">-</button>
      </div>
      <div class="row">
        <button onclick="calc('!')" class="scientific laptop">x!</button>
        <button onclick="calc('sin(')" class="scientific laptop normal">sin</button>
        <button onclick="calc('asin(')" class="scientific laptop inverse" style="display: none;">asin</button>
        <button onclick="calc('cos(')" class="scientific laptop normal">cos</button>
        <button onclick="calc('acos(')" class="scientific laptop inverse" style="display: none;">acos</button>
        <button onclick="calc('tan(')" class="scientific laptop normal">tan</button>
        <button onclick="calc('atan(')" class="scientific laptop inverse" style="display: none;">atan</button>
        <button onclick="calc('e')" class="scientific laptop">e</button>
        <button onclick="calc('E')" class="scientific laptop">EE</button>
        <button onclick="calc('1')">1</button>
        <button onclick="calc('2')">2</button>
        <button onclick="calc('3')">3</button>
        <button onclick="calc('+')" class="right">+</button>
      </div>
      <div class="row">
        <button onclick="calc('d')" class="scientific laptop radius-left" id="degree-btn">
          Deg
        </button>
        <button onclick="calc('r')" class="scientific laptop radius-left" id="radian-btn" style="display: none;">
          Rad
        </button>
        <button onclick="calc('sinh(')" class="scientific laptop">sinh</button>
        <button onclick="calc('cosh(')" class="scientific laptop">cosh</button>
        <button onclick="calc('tanh(')" class="scientific laptop">tanh</button>
        <button onclick="calc('π')" class="scientific laptop">π</button>
        <button onclick="calc('Rand')" class="scientific laptop">Rand</button>
        <button onclick="calc('0')" class="zero">0</button>
        <button onclick="calc('.')">.</button>
        <button onclick="calc('=')" class="right" id="radius-right">=</button>
      </div>
    </div>
    <script src="script.js"></script>
  </body>
</html>