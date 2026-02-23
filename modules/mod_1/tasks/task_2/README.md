## Полезная информация
### CSP
**[Content Security Policy (CSP)](https://developer.mozilla.org/ru/docs/Web/HTTP/Guides/CSP)** - это дополнительный уровень безопасности, позволяющий распознавать и устранять определённые типы атак, таких как Cross Site Scripting (XSS) и атаки внедрения данных. 

Для того чтобы включить CSP, необходимо настроить сервер так, чтобы в ответах он использовал HTTP-заголовок Content-Security-Policy

В качестве альтернативы настройке сервера, вы можете сконфигурировать CSP с помощью элемента <meta>. Например, так: `<meta http-equiv="Content-Security-Policy" content="default-src 'self'; img-src https://*; child-src 'none';">`

### Подключение локального шрифта через css файл
```css
@font-face {
  font-family: "Inter";
  src: url("/assets/fonts/Inter-VariableFont.woff2") format("woff2");
  font-weight: 100 900;   /* диапазон, а не одно число */
  font-style: normal;
  font-display: swap;
}

body {
  font-family: "Inter", system-ui, sans-serif;
}

h1 { font-weight: 750; }  /* можно любые значения внутри 100..900 */
```
