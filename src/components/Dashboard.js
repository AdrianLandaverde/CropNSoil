export default function Dashboard() {
    return (
      <div className="mt-8">
        <h2 className="font-semibold px-5" style={{ textDecorationLine: 'underline' }}>
          Farmers Dashboard
        </h2>
        <div className="text-lg px-5" style={{ textDecorationLine: 'none', display: 'flex', justifyContent: 'space-between' }}>
          <p style={{ display: 'inline' }} className="pr-20">Current Pattern</p>
          <p style={{ display: 'inline' }} className="pr-20">Crops</p>
          <p style={{ display: 'inline' }}>Expected Yield</p>
        </div>
      </div>
    );
  }
  