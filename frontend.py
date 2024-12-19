import React, { useState } from 'react';
import { RefreshCw } from 'lucide-react';
import { 
  LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer,
  BarChart, Bar, PieChart, Pie, Cell, RadarChart, Radar, PolarGrid,
  PolarAngleAxis, PolarRadiusAxis, Legend
} from 'recharts';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';

const SecurityDashboard = () => {
  // Sample data - replace with your backend API calls
  const [anomalyTrend] = useState([
    { timestamp: '08:00', anomalyScore: 20, devices: 240 },
    { timestamp: '09:00', anomalyScore: 25, devices: 245 },
    { timestamp: '10:00', anomalyScore: 45, devices: 242 },
    { timestamp: '11:00', anomalyScore: 30, devices: 248 },
    { timestamp: '12:00', anomalyScore: 65, devices: 238 },
    { timestamp: '13:00', anomalyScore: 35, devices: 247 }
  ]);

  const threatDistribution = [
    { name: 'Unauthorized Access', value: 35 },
    { name: 'Data Manipulation', value: 25 },
    { name: 'DDoS Attempts', value: 20 },
    { name: 'Protocol Violations', value: 15 },
    { name: 'Other', value: 5 }
  ];

  const deviceVulnerabilities = [
    { category: 'Authentication', value: 85 },
    { category: 'Encryption', value: 75 },
    { category: 'Access Control', value: 65 },
    { category: 'Data Integrity', value: 80 },
    { category: 'Physical Security', value: 70 }
  ];

  const networkMetrics = [
    { metric: 'Latency', value: 78 },
    { metric: 'Packet Loss', value: 12 },
    { metric: 'Signal Strength', value: 85 },
    { metric: 'Bandwidth Usage', value: 65 },
    { metric: 'Error Rate', value: 25 }
  ];

  const COLORS = ['#0088FE', '#00C49F', '#FFBB28', '#FF8042', '#8884d8'];

  return (
    <div className="p-6 space-y-6 bg-gray-50 min-h-screen">
      <div className="flex justify-between items-center">
        <h1 className="text-2xl font-bold">5G Network Security Analytics</h1>
        <button className="flex items-center gap-2 px-4 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600">
          <RefreshCw className="w-4 h-4" />
          Refresh Data
        </button>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* Anomaly Score and Device Count Trend */}
        <Card>
          <CardHeader>
            <CardTitle>Anomaly Score & Device Count Trend</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="h-[300px]">
              <ResponsiveContainer width="100%" height="100%">
                <LineChart data={anomalyTrend}>
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis dataKey="timestamp" />
                  <YAxis yAxisId="left" />
                  <YAxis yAxisId="right" orientation="right" />
                  <Tooltip />
                  <Legend />
                  <Line 
                    yAxisId="left"
                    type="monotone" 
                    dataKey="anomalyScore" 
                    stroke="#2563eb" 
                    strokeWidth={2}
                    name="Anomaly Score"
                  />
                  <Line 
                    yAxisId="right"
                    type="monotone" 
                    dataKey="devices" 
                    stroke="#10b981" 
                    strokeWidth={2}
                    name="Connected Devices"
                  />
                </LineChart>
              </ResponsiveContainer>
            </div>
          </CardContent>
        </Card>

        {/* Threat Distribution */}
        <Card>
          <CardHeader>
            <CardTitle>Threat Distribution</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="h-[300px]">
              <ResponsiveContainer width="100%" height="100%">
                <PieChart>
                  <Pie
                    data={threatDistribution}
                    cx="50%"
                    cy="50%"
                    labelLine={false}
                    label={({ name, percent }) => `${name} ${(percent * 100).toFixed(0)}%`}
                    outerRadius={100}
                    fill="#8884d8"
                    dataKey="value"
                  >
                    {threatDistribution.map((entry, index) => (
                      <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                    ))}
                  </Pie>
                  <Tooltip />
                </PieChart>
              </ResponsiveContainer>
            </div>
          </CardContent>
        </Card>

        {/* Device Security Assessment */}
        <Card>
          <CardHeader>
            <CardTitle>Device Security Assessment</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="h-[300px]">
              <ResponsiveContainer width="100%" height="100%">
                <RadarChart cx="50%" cy="50%" outerRadius="80%">
                  <PolarGrid />
                  <PolarAngleAxis dataKey="category" />
                  <PolarRadiusAxis angle={30} domain={[0, 100]} />
                  <Radar
                    name="Security Score"
                    dataKey="value"
                    data={deviceVulnerabilities}
                    fill="#2563eb"
                    fillOpacity={0.6}
                  />
                  <Legend />
                </RadarChart>
              </ResponsiveContainer>
            </div>
          </CardContent>
        </Card>

        {/* Network Performance Metrics */}
        <Card>
          <CardHeader>
            <CardTitle>Network Performance Metrics</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="h-[300px]">
              <ResponsiveContainer width="100%" height="100%">
                <BarChart data={networkMetrics}>
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis dataKey="metric" />
                  <YAxis domain={[0, 100]} />
                  <Tooltip />
                  <Legend />
                  <Bar dataKey="value" name="Score" fill="#10b981" />
                </BarChart>
              </ResponsiveContainer>
            </div>
          </CardContent>
        </Card>
      </div>
    </div>
  );
};

export default SecurityDashboard;
