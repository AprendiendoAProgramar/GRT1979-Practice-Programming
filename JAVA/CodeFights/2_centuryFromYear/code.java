int centuryFromYear(int year) {
   int resultado = year / 100;
   int resto = year % 100;
   if (resto == 0)
      return resultado;
   else
      return ++resultado;
}