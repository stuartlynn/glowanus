import type { NextPage } from "next";
import { useEffect, useState } from "react";
import styles from "../styles/Home.module.css";
import { format, formatDistance, formatRelative, subDays } from "date-fns";

type LastSeen = {
  deviceId: string;
  lastSeen: Date;
};


function statusColor(date: Date){
  let seen_since = (new Date().getTime() - date.getTime())/1000.0;
  if (seen_since < 5*60){
    return "green"
  }
  if (seen_since < 20*60){
    return 'yellow'
  }

  return 'red'

}

const Home: NextPage = () => {
  const [data, setData] = useState<Array<LastSeen> | null>(null);

  useEffect(() => {
    setInterval(() => {
      fetch("/api/recent_pings")
        .then((r) => r.json())
        .then((r) => {
          setData(
            r.map((r: any) => ({ ...r, lastSeen: new Date(r.lastSeen) }))
          );
        });
    }, 1000);
  }, []);

  return (
    <div className={styles.container}>
      <div
        style={{
          display: "grid",
          gridTemplateColumns: "repeat( auto-fit, 200px )",
          gap:"50px"
        }}
      >
        {data &&
          data.map((l) => (
            <div
              style={{
                backgroundColor: statusColor(l.lastSeen),
                border: "1px solid black",
                borderRadius: "20px",
                padding: "15px",
                boxSizing: "border-box",
                color: "white",
              }}
              key={l.deviceId}
            >
              <p>Device: {l.deviceId}</p>
              <p>
                Last seen:{" "}
                {formatDistance(l.lastSeen, new Date(), { addSuffix: true })}
              </p>
            </div>
          ))}
      </div>
    </div>
  );
};

export default Home;
