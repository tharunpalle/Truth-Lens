/**
 * Truth Lens - Client Foundation Script
 * Connects UI to backend foundation services and manages diagnostic state.
 */

document.addEventListener('DOMContentLoaded', () => {
  console.log('[Truth Lens] Foundation client initialized.');

  const healthEndpoint = '/api/health';
  const pingBtn = document.getElementById('btn-ping');
  const consoleOutput = document.getElementById('console-output');
  const statusLabel = document.querySelector('.status-label');

  async function checkHealth() {
    const startTime = performance.now();
    try {
      if (consoleOutput) {
        consoleOutput.textContent = `Connecting to ${healthEndpoint}...`;
      }
      const response = await fetch(healthEndpoint);
      const latency = Math.round(performance.now() - startTime);
      const data = await response.json();

      if (consoleOutput) {
        consoleOutput.textContent = JSON.stringify({
          ...data,
          latency: `${latency}ms`
        }, null, 2);
      }

      if (statusLabel) {
        statusLabel.textContent = `Operational (${latency}ms)`;
      }
    } catch (error) {
      if (consoleOutput) {
        consoleOutput.textContent = `[Error connecting to backend]: ${error.message}\nMake sure the local Python/Flask server is running.`;
      }
      if (statusLabel) {
        statusLabel.textContent = 'Offline / Standalone';
      }
    }
  }

  if (pingBtn) {
    pingBtn.addEventListener('click', (e) => {
      e.preventDefault();
      checkHealth();
    });
  }

  // Initial check on load
  checkHealth();
});
