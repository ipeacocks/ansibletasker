
        var output = document.getElementById('output');

        var xhr = new XMLHttpRequest();
        xhr.open('GET', '/ansible_stream');
        xhr.send();
        var position = 0;
        

        function handleNewData() {
            // the response text include the entire response so far
            // split the messages, then take the messages that haven't been handled yet
            // position tracks how many messages have been handled
            // messages end with a newline, so split will always show one extra empty message at the end
            var messages = xhr.responseText.split('\n');
            messages.slice(position, -1).forEach(function(value) {
                // build and append a new item to a list to log all output
                var item = document.createElement('p');
                item.textContent = value;
                output.appendChild(item);
            });
            position = messages.length - 1;

        }

        var timer;
        timer = setInterval(function() {
            // check the response for new data
            handleNewData();
            // stop checking once the response has ended
            if (xhr.readyState == XMLHttpRequest.DONE) {
                clearInterval(timer);

                document.getElementById("back_button").innerHTML ="<a href='/' class='btn btn-primary btn-block' role='button'><span class='glyphicon glyphicon-chevron-left'></span> Back</a>";

            }

        }, 1000);
