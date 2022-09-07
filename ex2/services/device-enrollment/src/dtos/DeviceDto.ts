export class DeviceDto {
  id: string;
  name: string;
  enrolledAt: Date;
  version: string;
  description: string;
  properties?: { [propName: string]: string };
}
