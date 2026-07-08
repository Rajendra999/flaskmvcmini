<!DOCTYPE html>
<html>

<head>

    <title>flaskmvcmini</title>

    <meta name="viewport" content="width=device-width, initial-scale=1">

</head>


<body>

<h1>
    Flask MVC Mini
</h1>


<!-- =====================================================
     STEP 001 : DATA TABLE
     ===================================================== -->

<table border="1">

    <tr>

        <th>ID</th>
        <th>Name</th>
        <th>Value</th>

    </tr>


    {% for row in data %}

    <tr>

        <td>{{ row.ID }}</td>
        <td>{{ row.Name }}</td>
        <td>{{ row.Value }}</td>

    </tr>

    {% endfor %}


</table>


</body>

</html>
