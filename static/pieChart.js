async function main() {
  // fetch the data from the endpoint we created
  const res = await fetch('http://127.0.0.1:5000/api/products/colour')
  const data = await res.json()

  // turn the data into arrays
  const colours = data.map(item => item.description) // ["Orange", "Navy", ...]
  const counts = data.map(item => item.count) // [17, 31, ...]

  // grab a reference to the canvas element on the page
  const ctx = document.getElementById('pieChart').getContext('2d')

  // create the chart
  // https://www.chartjs.org/docs/latest/charts/doughnut.html
  new Chart(ctx, {
    type: 'pie',
    data: {
      labels: colours,
      datasets: [
        {
          label: 'Product Colours',
          data: counts
        }
      ]
    },
    options: {
      responsive: true
    }
  })
}

// after the page has loaded, render the pie chart onto the page
document.addEventListener('DOMContentLoaded', main)
