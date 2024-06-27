/** @odoo-module **/
import {registry} from "@web/core/registry";
import {useService} from "@web/core/utils/hooks";
import {Component} from "@odoo/owl";

class SystrayIcon extends Component {
    setup() {
        super.setup(...arguments);
        this.action = useService("action");
        this.rpc = useService("rpc");
    }

    async _onClick() {
        let self = this;
        let action = await this.rpc("/web/dataset/call_kw/cart/open_cart", {
            model: 'cart',
            method: 'open_cart',
            args: [],
            kwargs: {}
        })
        return this.action.doAction(action, { clearBreadcrumbs: true });
    }
}

SystrayIcon.template = "systray_icon";
export const systrayItem = {Component: SystrayIcon,};
registry.category("systray").add("SystrayIcon", systrayItem, {sequence: 1000});



if ('mediaSession' in navigator) {

  navigator.mediaSession.metadata = new MediaMetadata({
    title: 'Never Gonna Give You Up',
    artist: 'Rick Astley',
    album: 'Whenever You Need Somebody',
    artwork: [
      { src: 'https://dummyimage.com/96x96',   sizes: '96x96',   type: 'image/png' },
      { src: 'https://dummyimage.com/128x128', sizes: '128x128', type: 'image/png' },
      { src: 'https://dummyimage.com/192x192', sizes: '192x192', type: 'image/png' },
      { src: 'https://dummyimage.com/256x256', sizes: '256x256', type: 'image/png' },
      { src: 'https://dummyimage.com/384x384', sizes: '384x384', type: 'image/png' },
      { src: 'https://dummyimage.com/512x512', sizes: '512x512', type: 'image/png' },
    ]
  });
}
