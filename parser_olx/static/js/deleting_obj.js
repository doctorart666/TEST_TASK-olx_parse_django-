function removeElem(delElem, attribute, attributeName) {
    //проверка на наличие всех аргументов.
      if (!(delElem && attribute && attributeName)) return;
    //возвращаем функцию, которая будет иметь доступ к аргументам, и при этом будет в себе хранить объект события.
      return function(e) {
     //Узнаем на каком элементе был произведен клик.
        let target = e.target;
    //Делаем проверку на наличие атрибута "data-del", и проверяем на наличие параметра "delete".
        if (!(target.hasAttribute(attribute) ?
            (target.getAttribute(attribute) === attributeName ? true : false) : false)) return;
        let elem = target;
    //После мы производим поиск элемента, который нужно удалить. Поиск идет снизу вверх. За счет того, что кнопки находяться внутри "card", то мы точно удалить нужный нам "card"(сорри за тавтологию).
        while (target != this) {
          if (target.classList.contains(delElem)) {
            target.remove();
            return;
          }
          target = target.parentNode;
        }
        return;
      };
    }


    document.addEventListener("click", removeElem("card", "data-del", "delete", "line"));