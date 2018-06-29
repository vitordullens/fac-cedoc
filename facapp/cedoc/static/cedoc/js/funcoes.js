function hideAndShow(str){
                // clear inputs
                document.getElementById('id_File').value = ""
                document.getElementById('id_url').value = ""

                // erase both fields
                document.getElementById('File').classList.add('hidden');
                document.getElementById('url').classList.add('hidden');

                // show correct one, blank
                if(str != '')
                    document.getElementById(str).classList.remove('hidden');
            }

            function myConfirm(str){
                if (confirm(str))
                    location.href = "{% url 'url_delete' doc.id %}";
            }

            var month = {};
            month["Janeiro"] = "01";
            month["Fevereiro"] = "02";
            month["Março"] = "03";
            month["Abril"] = "04";
            month["Maio"] = "05";
            month["Junho"] = "06";
            month["Julho"] = "07";
            month["Agosto"] = "08";
            month["Setembro"] = "09";
            month["Outubro"] = "10";
            month["Novembro"] = "11";
            month["Dezembro"] = "12";