async function main() {
  const res = await fetch('http://localhost:5000/api/products/colour')
  const data = await res.json()

  const colours = data.map(item => item.description)
  const counts = data.map(item => item.count)

  const ctx = document.getElementById('pieChart').getContext('2d')

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

document.addEventListener('DOMContentLoaded', main)
