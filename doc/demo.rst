================
Interactive demo
================

.. raw:: html

    <form id="form"></form>

    <img id="turkshead" src="data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==" alt="A Turk's head knot" class="img-responsive"/>

    <script type="text/javascript">
      function updateImage() {
        $('#turkshead').attr('src', 'https://dyn.vincent-jacques.net/turkshead?' + $("#form").serialize())
      }

      $.getJSON("https://dyn.vincent-jacques.net/turkshead/parameters", function(parameters) {
        const form = $('#form')

        parameters.forEach(function(parameter) {
          if (parameter.suggested_values.length > 1) {
            const label = `<label for="${parameter.name}">${parameter.description}</label>`
            const options = parameter.suggested_values.map(v => `<option${v === parameter.default_value ? ' selected' : ''}>${v}</option>`).join('')
            const select = `<select id="${parameter.name}" name="${parameter.name}">${options}</select>`
            form.append(`${label}&nbsp;${select}<br />`)
            $(`#${parameter.name}`).change(updateImage)
          }
        })

        updateImage()
      })
    </script>

No effort has been made to avoid "clashes".
If you see steps where the lines cross, try reducing the line width.
