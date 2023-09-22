    // Obtém uma referência ao elemento de entrada de data
        var inputDate = document.getElementById("dat");

        // Obtém a data atual
        var dataAtual = new Date();

        // Formata a data atual no formato "YYYY-MM-DD"
        var dataFormatada = dataAtual.toISOString().split('T')[0];

        // Define o atributo "min" do elemento de entrada de data para a data atual
        inputDate.setAttribute("min", dataFormatada);
        // Obtém uma referência ao elemento de entrada de data
        var inputDate = document.getElementById("date");

        // Obtém a data atual
        var dataAtual = new Date();

        // Formata a data atual no formato "YYYY-MM-DD"
        var dataFormatada = dataAtual.toISOString().split('T')[0];

        // Define o atributo "min" do elemento de entrada de data para a data atual
        inputDate.setAttribute("min", dataFormatada);